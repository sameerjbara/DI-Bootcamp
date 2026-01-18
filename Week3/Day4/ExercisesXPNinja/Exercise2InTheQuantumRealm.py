# Instructions
# Write a class called QuantumParticle and implement the following:
# The attributes - The particle has an initial position (x), momentum (y) and spin (p)

# The method position() - Position measurement: generate a random position (integer between 1 and 10,000)

# The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0 and 1)

# The method spin() - Spin measurement: can randomly be 1/2 or -1/2

# Create a method that implements a disturbance. A disturbance occurs each time a measurement is made (e.g. one of the measurements method is called). Disturbance changes the position and the momentum of the particle (randomly generated) and then prints ‘Quantum Interferences!!’

# Implement a meaningful representation of the particle (repr)

# Quantum Entanglement: two particle can be entangled, meaning that if I measure the spin of one of them the second one is automatically set to the opposite value. A quantum particle can only be entangled to another quantum particle (check that when you run the method !!)
# Modify as you see fit the attributes and methods of your class to fit the previous definition
# When two particles are entangled print: ‘Spooky Action at a Distance !!’
# >>>p1 = QuantumParticle(x=1,p=5.0)
# >>>p2 = QuantumParticle(x=2,p=5.0)
# >>>p1.entangle(p2)
# >>>'Particle p1 is now in quantum entanglement with Particle p2'
# >>>p1 = QuantumParticle()
# >>>p2 = QuantumParticle()
# >>>p1.entangle(p2)
# >>>'Spooky Action at a Distance'



import random


class QuantumParticle:
    def __init__(self, x=None, p=None, s=None, name=None):
        self.x = x if x is not None else random.randint(1, 10_000)
        self.p = p if p is not None else random.random()
        self.s = s if s is not None else random.choice([0.5, -0.5])

        self.name = name
        self._entangled_with = None

    def _disturb(self):
        self.x = random.randint(1, 10_000)
        self.p = random.random()
        print("Quantum Interferences!!")

    def position(self):
        self._disturb()
        self.x = random.randint(1, 10_000)
        return self.x

    def momentum(self):
        self._disturb()
        self.p = random.random()
        return self.p

    def spin(self):
        self._disturb()
        self.s = random.choice([0.5, -0.5])

        if self._entangled_with is not None:
            self._entangled_with.s = -self.s

        return self.s

    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle.")

        self._entangled_with = other
        other._entangled_with = self

        if self.name and other.name:
            return f"Particle {self.name} is now in quantum entanglement with Particle {other.name}"

        print("Spooky Action at a Distance")

    def __repr__(self):
        partner = None
        if self._entangled_with is not None:
            partner = self._entangled_with.name if self._entangled_with.name else "QuantumParticle"
        return f"QuantumParticle(x={self.x}, p={self.p:.4f}, s={self.s}, entangled_with={partner})"


# Demo
if __name__ == "__main__":
    p1 = QuantumParticle(x=1, p=5.0, name="p1")
    p2 = QuantumParticle(x=2, p=5.0, name="p2")
    print(p1.entangle(p2))

    p3 = QuantumParticle(name="p3")
    p4 = QuantumParticle(name="p4")
    p3.entangle(p4)

    print("p3 spin:", p3.spin())
    print("p4 spin (should be opposite):", p4.s)
    print(p3)
    print(p4)
