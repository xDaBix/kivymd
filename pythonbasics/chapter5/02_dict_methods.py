
d={} #empty dict
marks={
    "harry":90,
    "manan":99,
    "varun":98
}
marks.update({"harry":89})
print(marks.keys())
print(marks.values())


print(marks.get("harry"))#prints none
print(marks["harry"])# returns an error
