
class Person:
    def __init__(self, name = 'default', skills = []):
        self.name = name
        self.skills = skills
    def person_info(self):
        return f'{self.name}'
    def add_skill(self, skill):
        self.skills.append(skill)
p = Person('Charlie')
print(p)
print(p.name)
print(p.person_info())

dp = Person()
print(dp.person_info())

p.add_skill('Skin')

print(p.skills)

class Student(Person):
    def __init__(self, name='default', skills=[], gender='male'):
        self.gender = gender
        super().__init__(name, skills)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.name}, {gender} is good at {self.skills}'
s1 = Student('yu', 'swimming')
print(s1.person_info())

class Statistics:
    def __init__(self, data = []):
        self.data = data
    def count(self):
        return len(self.data)
    def sum(self):
        s = 0
        for i in self.data:
            s += i
        return s
    def min(self):
        min = self.data[0]
        for i in self.data:
            min = i if i < min else min
        return min
    def max(self):
        max = self.data[0]
        for i in self.data:
            max = i if i > max else max
        return max
    def mode(self):
        from collections import Counter
        c = Counter(self.data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid-1] + self.data[mid]) / 2
        return self.data[mid]
    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()
    def std(self):
        import math
        return math.sqrt(self.variance())
    def frequency_dist(self):
        from collections import Counter
        return dict(Counter(self.data))
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.variance()) # 17.5
print('Frequency Distribution: ', data.frequency_dist())


class PersonAccount:
    def __init__(self, firstname = '', lastname = '', incomes = 0, expenses = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def add_income(self, add):
        self.incomes += add
    
p = PersonAccount()
p.add_income(100)
print(p.incomes)