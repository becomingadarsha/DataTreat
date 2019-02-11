from django import template

register = template.Library()

problems = ["Gastric", "Eye Problem", "Heart Diseases", "Kidney", "Lung", "Other Major Operation", "Stone", None]
avgDbtRates = ["100-110", "110-125", "125-140", "140-155", "155+"]
bpLevels = ["110-125", "125-150", "150-165", "165+"]
diabetes_types = ["Type-1 (Juvenile-onset)", "Type-2 (Non-insulin dependent or Adult-onset)", "Type-3 (Gestational)"]

vitaminCs = ["<0.2", "0.6+", "0.2+0.6"]
bloodKets = ["<0.6", "1.5+", "0.6-1.5"]
uroporphytrins = ["2.4+", "<2.4"]
blood_bilburins = ["0.3+", "<0.3"]
rbc_cnts = ["<4.7", "6.4+", "4.7-6.4"]
blood_urea_nits = ["<7", "20+", "7-20"]
wbc_cnts = ["<4000", "7000+", "4000-7000"]
cyroproteins = ["<30", "30+"]

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
def toDiabetesType(val):
    return diabetes_types[val]

@register.filter
def toBPLevel(val):
    return bpLevels[val]

@register.filter
def toVitaminC(val):
    return vitaminCs[val]

@register.filter
def toBloodKetones(val):
    return bloodKets[val]

@register.filter
def toUroporphytrins(val):
    return uroporphytrins[val]

@register.filter
def toBloodBilburins(val):
    return blood_bilburins[val]

@register.filter
def toRBCCounts(val):
    return rbc_cnts[val]

@register.filter
def toBloodUreaNet(val):
    return blood_urea_nits[val]

@register.filter
def toWBCCounts(val):
    return wbc_cnts[val]

@register.filter
def toCyroproteins(val):
    return cyroproteins[val]
