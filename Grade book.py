
import pytest
"""
HAZ FUNCIÓN PARA QUE
ENCUENTRE EL PROMEDIO DE LAS TRES
PUNTUACIONES PASADAS A ELLA Y
DEVUELVA EL VALOR DE LA LETRA
ASOCIADO CON ESA CALIFICACIÓN.
PUNTUACIÓN NUMÉRICA CALIFICACIÓN
en Letra
90 <= promedio <= 100 'A'
80 <= promedio < 90 'B'
70 <= promedio < 80 'C'
60 <= promedio < 70 'D'
0 <= promedio < 60 'F'
"""


def get_grade(score1, score2, score3):
    promedio = (score1 + score2 + score3)/3
    if 90 <= promedio <= 100:
       return 'A'
    elif 80 <= promedio < 90:
       return 'B'
    elif 70 <= promedio < 80:
       return 'C'
    elif 60 <= promedio < 70:
       return 'D'
    else:
       return 'F'




class TestGradeBook:
    def test_a(self):
        assert get_grade(95, 90, 93) == "A", "get_grade(95, 90, 93)"
        assert get_grade(100, 85, 96) == "A", "get_grade(100, 85, 96)"
        assert get_grade(92, 93, 94) == "A", "get_grade(92, 93, 94)"
        assert get_grade(100, 100, 100) == "A", "get_grade(100, 100, 100)"

    def test_b(self):
        assert get_grade(70, 70, 100) == "B", "get_grade(70, 70, 100)"
        assert get_grade(82, 85, 87) == "B", "get_grade(82, 85, 87)"
        assert get_grade(84, 79, 85) == "B", "get_grade(84, 79, 85)"

    def test_c(self):
        assert get_grade(70, 70, 70) == "C", "get_grade(70, 70, 70)"
        assert get_grade(75, 70, 79) == "C", "get_grade(75, 70, 79)"
        assert get_grade(60, 82, 76) == "C", "get_grade(60, 82, 76)"

    def test_d(self):
        assert get_grade(65, 70, 59) == "D", "get_grade(65, 70, 59)"
        assert get_grade(66, 62, 68) == "D", "get_grade(66, 62, 68)"
        assert get_grade(58, 62, 70) == "D", "get_grade(58, 62, 70)"

    def test_f(self):
        assert get_grade(44, 55, 52) == "F", "get_grade(44, 55, 52)"
        assert get_grade(48, 55, 52) == "F", "get_grade(48, 55, 52)"
        assert get_grade(58, 59, 60) == "F", "get_grade(58, 59, 60)"
        assert get_grade(0, 0, 0) == "F", "get_grade(0, 0, 0)"
