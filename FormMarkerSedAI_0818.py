
# Function to read VitalDB file and return a pandas DataFrame
def read_vitaldb_file(file_path):
    # Read VitalDB file
    Tracks =vitaldb.vital_trks(file_path)
    vf = vitaldb.VitalFile(file_path)
    
    #Splitting Tracks with DoubleValues
    original_track_name = 'Intellivue/EEG'
    new_track_name_one = 'Intellivue/EEG_1'
    new_track_name_two = 'Intellivue/EEG_2'
    vf = split_track_samples_and_add_track(vf, original_track_name, new_track_name_one, new_track_name_two)
    Tracks.remove(original_track_name)
    Tracks.extend([new_track_name_one, new_track_name_two])
    df= vf.to_pandas(track_names=Tracks, interval=1/200, return_datetime=True)
    return df

def split_track_samples_and_add_track(vf : vitaldb.VitalFile, dtname : str, name_first_track : str, name_sec_track : str):
    """split one Track into two different if there are double values at one dt
    :param vf: VitalFile Objekt with loaded vital file
    :param dtname: original track name to be splitted
    :param name_first_track: name of the new first track
    :param Name_sec_track: name of the new secound track 
    """
    trk = vf.find_track(dtname)
    # {dt:... , val:...} structur of the elements in the array
    dict_track_1 = []   
    dict_track_2 = []
    current_dt = 0 # counter to check wether there are two values at one timestamp
    for rec in trk.recs:

        if current_dt == rec['dt']:
            dict_track_2.append(rec)
        else:
            current_dt = rec['dt']
            dict_track_1.append(rec)

    # add new Track with first packet values
    vf.add_track(name_first_track , dict_track_1 , trk.srate, trk.unit, trk.mindisp, trk.maxdisp )
    vf.add_track(name_sec_track,  dict_track_2 , trk.srate,  trk.unit, trk.mindisp, trk.maxdisp)

    # set correct Track Parameter
    vf.trks[name_first_track].fmt = trk.fmt
    vf.trks[name_sec_track].fmt = trk.fmt

    vf.trks[name_first_track].gain = trk.gain
    vf.trks[name_sec_track].gain = trk.gain

    vf.trks[name_first_track].offset = trk.offset
    vf.trks[name_sec_track].offset = trk.offset

    vf.trks[name_first_track].col = trk.col
    vf.trks[name_sec_track].col = trk.col

    vf.trks[name_first_track].montype = trk.montype
    vf.trks[name_sec_track].montype = trk.montype

    # delete old primary Track
    vf.remove_track(dtname) 
    return vf
