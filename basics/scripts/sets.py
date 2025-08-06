
# Set
# type of collection
# unordered
# unique elements

set1 = {1, 2, 3, 4, 5, 5}
print(set1)

print(set([1, 2, 2, 3, 3, 3, 4, 5]))

setA = {"a", "b", "c"}
setA.remove("c")
print("c" in setA)

setA.add("c")
setB = {     "b", "c", "d"}

print(setA & setB) # Intersection
print(setA.difference(setB))
print(setB.difference(setA))
print(setA.intersection(setB))

setC = setA.union(setB)
print(setC)
print(len(setC))

print({"a"}.issubset(setC))
print({"a"}.issuperset(setC))