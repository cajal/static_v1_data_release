"""
Static scan nda schema classes and methods
"""
import numpy as np
import datajoint as dj

schema = dj.schema('static_release_nda', create_tables=True)
schema.spawn_missing_classes()

@schema
class Scan(dj.Manual):
    """
    Class methods not available outside of BCM pipeline environment
    """
    definition = """
    # Information on completed scan
    session              : smallint                     # Session ID
    scan_idx             : smallint                     # Scan ID
    ---
    nframes              : int                          # number of frames per scan
    nfields              : tinyint                      # number of fields per scan
    fps                  : float                        # frames per second (Hz)
    """
    
    static_scans = [
       {'animal_id': 21067, 'session': 10, 'scan_idx': 18, 'pipe_version': 1, 'field': 1},
       {'animal_id': 21067, 'session': 13, 'scan_idx': 14, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22620, 'session': 4, 'scan_idx': 15, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22620, 'session': 4, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22620, 'session': 5, 'scan_idx': 11, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22846, 'session': 2, 'scan_idx': 19, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22846, 'session': 2, 'scan_idx': 21, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22846, 'session': 7, 'scan_idx': 15, 'pipe_version': 1, 'field': 1},
       {'animal_id': 22846, 'session': 10, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23343, 'session': 5, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23555, 'session': 5, 'scan_idx': 12, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23602, 'session': 2, 'scan_idx': 13, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23602, 'session': 3, 'scan_idx': 8, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23603, 'session': 3, 'scan_idx': 14, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23604, 'session': 1, 'scan_idx': 17, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23604, 'session': 1, 'scan_idx': 19, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23604, 'session': 2, 'scan_idx': 9, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23604, 'session': 2, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23605, 'session': 1, 'scan_idx': 16, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23618, 'session': 2, 'scan_idx': 13, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23656, 'session': 14, 'scan_idx': 22, 'pipe_version': 1, 'field': 1},
       {'animal_id': 23964, 'session': 4, 'scan_idx': 22, 'pipe_version': 1, 'field': 1}
                    ]
        
    @property
    def key_source(self):
        return (meso.experiment.Scan * meso.ScanInfo).proj('filename', 'nfields', 'nframes', 'fps') & self.static_scans
    
    @classmethod
    def fill(cls):
        cls.insert(cls.key_source, ignore_extra_fields=True)
