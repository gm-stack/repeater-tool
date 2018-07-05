import os
import csv

def output(category, items):
	name = "-".join(category)
	f = open(os.path.join('icom_out', name + '.csv'), 'w')
	wr = csv.writer(f)
	wr.writerow(['CH No','Name','SEL','Frequency','Dup','Offset',
			     'Mode','DATA','Filter','TONE','Repeater Tone',
			     'TSQL Frequency','DTCS Code','DTCS Polarity',
			     'DV SQL','DV CSQL Code','Your Call Sign',
			     'RPT1 Call Sign','RPT2 Call Sign','Split'])

	for i,item in enumerate(items):
		out_freq = float(item['Output'])
		in_freq = float(item['Input'])
		if in_freq == out_freq:
			duplex = 'OFF'
		elif in_freq > out_freq:
			duplex = 'DUP+'
		else:
			duplex = 'DUP-'
		offset = abs(out_freq - in_freq)
		tone = float(item['Tone']) if item['Tone'] != '-' else None

		wr.writerow([
			i, # CH No
			(item['Call'][2] + item['Call'][4:] + ' ' + item['Location'])[:16], # Name
			'ON', # SEL
			"%.6f" % out_freq, # Frequency
			duplex, # Dup
			"%.6f" % offset, # Offset
			category[2], # Mode
			'OFF', # DATA
			'1', # Filter
			'TONE' if tone else 'OFF', # TONE
			"%.1fHz" % (tone or 67.0), # Repeater Tone
			"%.1fHz" % (tone or 67.0), # TSQL Frequency
			'023', # DTCS Code
			'BOTH N', # DTCS Polarity
			'OFF', # DV SQL
			'0', # DV CSQL Code
			'', # Your Call Sign
			'', # RPT1 Call Sign
			'', # RPT2 Call Sign
			'OFF'  # Split
			])

	f.close()

#Output,Input,Call,mNemonic,Location,Service Area,Latitude,Longitude,S,ERP,HASL,T/O,Sp,Tone,Notes
