"""
Static scan nda schema classes and methods
"""
import numpy as np
import datajoint as dj
from pipeline import meso

schema = dj.schema('static_release_nda', create_tables=True)
schema.spawn_missing_classes()

@schema
class Scan(dj.Manual):
    """
    Class methods not available outside of BCM pipeline environment
    """
    definition = """
    # Information on completed scan
    animal_id            : int                          # Animal ID
    session              : smallint                     # Session ID
    scan_idx             : smallint                     # Scan ID
    ---
    nframes              : int                          # number of frames per scan
    nfields              : tinyint                      # number of fields per scan
    fps                  : float                        # frames per second (Hz)
    """
    
    # unfiltered, contain animals with autistic phenotypes, delete before release
#     static_scans = [
#        {'animal_id': 21067, 'session': 10, 'scan_idx': 18, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 21067, 'session': 13, 'scan_idx': 14, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22620, 'session': 4, 'scan_idx': 15, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22620, 'session': 4, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22620, 'session': 5, 'scan_idx': 11, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22846, 'session': 2, 'scan_idx': 19, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22846, 'session': 2, 'scan_idx': 21, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22846, 'session': 7, 'scan_idx': 15, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 22846, 'session': 10, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23343, 'session': 5, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23555, 'session': 5, 'scan_idx': 12, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23602, 'session': 2, 'scan_idx': 13, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23602, 'session': 3, 'scan_idx': 8, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23603, 'session': 3, 'scan_idx': 14, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23604, 'session': 1, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23604, 'session': 1, 'scan_idx': 19, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23604, 'session': 2, 'scan_idx': 9, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23604, 'session': 2, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23605, 'session': 1, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23618, 'session': 2, 'scan_idx': 13, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23656, 'session': 14, 'scan_idx': 22, 'pipe_version': 1, 'field': 1},
#        {'animal_id': 23964, 'session': 4, 'scan_idx': 22, 'pipe_version': 1, 'field': 1}
#                     ]
    
    static_scans = [
       {'animal_id': 21067, 'session': 9, 'scan_idx': 17, 'pipe_version': 1, 'group_id': 29, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '21067-9-1'},
       {'animal_id': 21067, 'session': 10, 'scan_idx': 18, 'pipe_version': 1, 'group_id': 35, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '21067-10-25'},
       {'animal_id': 21067, 'session': 13, 'scan_idx': 14, 'pipe_version': 1, 'group_id': 38, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '21067-13-2'},
       {'animal_id': 22620, 'session': 4, 'scan_idx': 15, 'pipe_version': 1, 'group_id': 55, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22620-4-16'},
       {'animal_id': 22620, 'session': 4, 'scan_idx': 17, 'pipe_version': 1, 'group_id': 69, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22620-4-16'},
       {'animal_id': 22620, 'session': 5, 'scan_idx': 11, 'pipe_version': 1, 'group_id': 70, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22620-5-14'},
       {'animal_id': 22846, 'session': 2, 'scan_idx': 19, 'pipe_version': 1, 'group_id': 60, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22846-2-20'},
       {'animal_id': 22846, 'session': 2, 'scan_idx': 21, 'pipe_version': 1, 'group_id': 73, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22846-2-20'},
       {'animal_id': 22846, 'session': 7, 'scan_idx': 15, 'pipe_version': 1, 'group_id': 72, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22846-7-14'},
       {'animal_id': 22846, 'session': 10, 'scan_idx': 16, 'pipe_version': 1, 'group_id': 74, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '22846-10-17'},
       {'animal_id': 23343, 'session': 5, 'scan_idx': 17, 'pipe_version': 1, 'group_id': 88, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '23343-5-22'},
       {'animal_id': 23555, 'session': 5, 'scan_idx': 12, 'pipe_version': 1, 'group_id': 106, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '23555-5-13'},
       {'animal_id': 23656, 'session': 14, 'scan_idx': 22, 'pipe_version': 1, 'group_id': 142, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '23656-14-18'},
       {'animal_id': 23964, 'session': 4, 'scan_idx': 22, 'pipe_version': 1, 'group_id': 163, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '23964-4-23'},
       {'animal_id': 26644, 'session': 14, 'scan_idx': 17, 'pipe_version': 1, 'group_id': 236, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '26644-14-18', 'album_id': 3},
       {'animal_id': 26645, 'session': 2, 'scan_idx': 18, 'pipe_version': 1, 'group_id': 237, 'segmentation_method': 6, 'spike_method': 5, 'preproc_id': 0, 'stack': '26645-2-19', 'album_id': 3}]
        
    @property
    def key_source(self):
        return (meso.experiment.Scan * meso.ScanInfo).proj('filename', 'nfields', 'nframes', 'fps') & self.static_scans
    
    @classmethod
    def fill(cls):
        cls.insert(cls.key_source, ignore_extra_fields=True)
