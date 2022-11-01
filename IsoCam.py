import numpy as np
from math import sin, cos


class IsoCam:
    _TRANSLATION_MATRIX = np.matrix([
        [1, 0, 0],
        [0, 1, 0],
    ])
    _SIMPLE_TRANSLATION = False

    _ROTATION_MATRIX = np.matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    _mapping_matrix = _TRANSLATION_MATRIX @ _ROTATION_MATRIX

    def _map_point(self, point):
        if self._SIMPLE_TRANSLATION:
            return np.matrix([point[0], point[1]])
        return self._TRANSLATION_MATRIX @ point

    def point_on_screen(self, point):

        return self._mapping_matrix @ point

    '''
    |YAW   / ROLL
    |    /
    |  /
    |/______ PITCH
    '''
    yaw, pitch, roll = 0, 0, 0

    def map_rotation(self):
        a,b,c = self.roll, self.yaw, self.pitch
        if self._SIMPLE_TRANSLATION:
            self._ROTATION_MATRIX = np.matrix([
                [cos(a)*cos(b), cos(a)*sin(b)*sin(c)-sin(a)*cos(c), cos(a)*sin(b)*cos(c)+sin(a)*sin(c)],
                [sin(a)*cos(b), sin(a)*sin(b)*sin(c)+cos(a)*cos(c), sin(a)*sin(b)*cos(c)-cos(a)*sin(c)],
                [0, 0, 0]
            ])
        else:
            self._ROTATION_MATRIX = np.matrix([
                [cos(a)*cos(b), cos(a)*sin(b)*sin(c)-sin(a)*cos(c), cos(a)*sin(b)*cos(c)+sin(a)*sin(c)],
                [sin(a)*cos(b), sin(a)*sin(b)*sin(c)+cos(a)*cos(c), sin(a)*sin(b)*cos(c)-cos(a)*sin(c)],
                [-sin(b), cos(b)*sin(c), cos(b)*cos(c)]
            ])
        self._mapping_matrix = self._TRANSLATION_MATRIX @ self._ROTATION_MATRIX
