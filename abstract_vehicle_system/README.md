# Abstract Vehicles Project in Python

This project demonstrates the use of **abstract classes** in Python using the `abc` module. It implements an abstract base class `Vehicle` and two concrete subclasses: `Car` and `Motorcycle`.

---

## Description

The project shows how to create **abstract methods** that must be implemented in subclasses and how to define specific behaviors for each type of vehicle.  

- **Vehicle**: Abstract class that defines `start()` and `stop()` as mandatory methods.
- **Car**: Concrete subclass that implements start and stop methods with specific messages.
- **Motorcycle**: Concrete subclass that implements start and stop methods with specific messages.

---

## Features

- Start and stop vehicles.
- Prevent starting a vehicle that is already on or stopping a vehicle that is already off.
- Demonstrates **inheritance** and **polymorphism**.

---

## Code Structure

```text
Vehicle (abstract class)
├─ Car (concrete subclass)
└─ Motorcycle (concrete subclass)

```bush
python abstract_vehicle_system.py