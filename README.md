# VitalRecorder Software Bugfix: EEG waves from PHILIPS Intellivue Patient monitor on a single track 

When recording EEG data from PHILIPS Intellivue Monitors with VitalRecorder (https://vitaldb.net/vital-recorder/) both waveforms are written to a single track. 
While the data of both signals is saved in the *.vital file format, using the VitalRecorder software or the python API only a single waveform can be exported.

## Usage
Given the filepath of the VITAL file, the function extracts the EEG data and splits it into two seperate tracks which are added to the VITAL file together with necessary track information. The original EEG tracks is deleted.

## LICENSE
See license document.

## Contact information
The function was written by XXX (XXXX@XXX.de)
as part of a multicenter biosignal data acqusition project lead by Dr. Jakob Garbe, MD (jakob.garbe@uk-halle.de).
