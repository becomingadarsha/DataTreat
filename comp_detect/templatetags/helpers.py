from django import template

register = template.Library()

problems = ["Gastric", "Eye Problem", "Heart Diseases", "Kidney", "Lung", "Other Major Operation", "Stone", None]
avgDbtRates = ["100-110", "110-125", "125-140", "140-155", "155+"]
bpLevels = ["110-125", "125-150", "150-165", "165+"]

@register.filter
def toColor(prob):
    if(prob >= 0.5):
        return "text-danger"
    elif(prob < 0.5 and prob > 0.1):
        return "text-warning"
    else:
        return "text-success"

@register.filter
def toGender(val):
    return "Female" if val == 0 else "Male"

@register.filter
def toProblem(val):
    return problems[val]

@register.filter
def toAvgDbtRates(val):
    return avgDbtRates[val]

@register.filter
def toBPLevel(val):
    return bpLevels[val]
