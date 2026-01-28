from dataclasses import dataclass

@dataclass
class person:
    name: str
    age: int
    email: str
    phone: str
    address: str

p1 = person("john", 30, "john@example.com", "1234567890", "123 Main St")
print(p1.name)
print(p1.age)
print(p1.email)
print(p1.phone)
print(p1.address)