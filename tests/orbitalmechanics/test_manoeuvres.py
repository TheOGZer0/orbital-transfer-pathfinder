from unittest import TestCase

import orbitalmechanics.bodies
import orbitalmechanics.orbits
import orbitalmechanics.manoeuvres


# Normally, testing abstract classes is not standard practice.
# In this case, there's some quite essential behaviour that would be strange to test in concrete subclasses.
# Because module modularity is based on creating many subclasses of BaseManoeuvre.

class TestBaseManoeuvre(TestCase):

    # Concrete implementation of Abstract BaseManoeuvre so that objects can be initialized.
    # Abstract methods must be implemented, but these don't have to be tested.
    class ConcreteManoeuvre(orbitalmechanics.manoeuvres.BaseManoeuvre):
        def _delta_v(self, insect_r):
            return insect_r * 10

        @staticmethod
        def evaluate(orbit1: orbitalmechanics.orbits.Orbit, orbit2: orbitalmechanics.orbits.Orbit) -> bool:
            return True

    # Actual tests
    def setUp(self):
        self.central_body = orbitalmechanics.bodies.CentralBody(0, 0, 0, 0)
        self.orbit1 = orbitalmechanics.orbits.Orbit(self.central_body, apo=1000, per=1000)
        self.orbit2 = orbitalmechanics.orbits.Orbit(self.central_body, apo=2000, per=2000)

        self.testcase = TestBaseManoeuvre.ConcreteManoeuvre(self.orbit1, self.orbit2, 555)

    def test_constructor(self):
        self.assertEqual(len(self.orbit1.manoeuvres), 1,
                         "BaseManoeuvre constructor should add self to orbit1.manoeuvres.")

        self.assertEqual(len(self.orbit2.manoeuvres), 1,
                         "BaseManoeuvre constructor should add self to orbit2.manoeuvres.")

        self.assertEqual(5550, self.testcase.dv,
                         """BaseManoeuvre constructor should pass insect_r to
_delta_v() that's implemented by subclass to compute Delta-V.""")

    def test_get_other(self):
        self.assertEqual(self.testcase.get_other(self.orbit1), self.orbit2,
                         "BaseManoeuvre.get_other() should return orbit2 when passed orbit1.")

        self.assertEqual(self.testcase.get_other(self.orbit2), self.orbit1,
                         "BaseManoeuvre.get_other() should return orbit1 when passed orbit2.")


class TestProRetroGradeManoeuvre(TestCase):

    def setUp(self):
        self.earth = orbitalmechanics.bodies.CentralBody(5.972E24,
                                                         6371000,
                                                         200000,
                                                         3.986004418E14)

    def test__delta_v(self):
        self.fail()

    def test_evaluate(self):
        orbit_1_testcase_1 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=10000,
                                                           per=10000,
                                                           i=60)

        orbit_2_testcase_1 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=20000,
                                                           per=10000,
                                                           i=60)

        self.assertTrue(orbitalmechanics.manoeuvres.ProRetroGradeManoeuvre.evaluate(orbit_1_testcase_1,
                                                                                    orbit_2_testcase_1),
                        msg="ProRetroGradeManoeuvre should evaluate as possible between 2 orbits"
                            "that share an apside and inclination.")

        orbit_1_testcase_2 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=10000,
                                                           per=10000,
                                                           i=0)

        orbit_2_testcase_2 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=20000,
                                                           per=10000,
                                                           i=60)

        self.assertFalse(orbitalmechanics.manoeuvres.ProRetroGradeManoeuvre.evaluate(orbit_1_testcase_2,
                                                                                     orbit_2_testcase_2),
                        msg="ProRetroGradeManoeuvre should evaluate as impossible between 2 orbits"
                            "that share an apside, but don't share their inclination.")

        orbit_1_testcase_3 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=10000,
                                                           per=10000,
                                                           i=60)

        orbit_2_testcase_3 = orbitalmechanics.orbits.Orbit(self.earth,
                                                           apo=20000,
                                                           per=20000,
                                                           i=60)

        self.assertFalse(orbitalmechanics.manoeuvres.ProRetroGradeManoeuvre.evaluate(orbit_1_testcase_3,
                                                                                     orbit_2_testcase_3),
                         msg="ProRetroGradeManoeuvre should evaluate as impossible between 2 orbits"
                             "that share their inclination but don't share an apside.")


class TestInclinationChange(TestCase):

    def setUp(self):
        self.earth = orbitalmechanics.bodies.CentralBody(5.972E24,
                                                         6371000,
                                                         200000,
                                                         3.986004418E14)

    def test__delta_v(self):
        self.fail()

    def test_evaluate(self):
        self.fail()


class TestInclinationAndProRetroGradeManoeuvre(TestCase):

    def setUp(self):
        self.earth = orbitalmechanics.bodies.CentralBody(5.972E24,
                                                         6371000,
                                                         200000,
                                                         3.986004418E14)

    def test__delta_v(self):
        self.fail()

    def test_evaluate(self):
        self.fail()