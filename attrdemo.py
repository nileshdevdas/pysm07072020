# the attribute libraries
# transparently define the goal of implementing constructor
# attributes
import attr


@attr.s
class Employee(object):
    id = attr.ib()


emp = Employee(1)
# i declared a id as field in object
# attr.ib() there attribute in object id

