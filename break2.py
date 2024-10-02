text = "Friss és boldog vagyok"
for x in text: 
    if x.lower() in "aáeéoóöőuúüű":
        break
    else:
        print(x, end=", ")
print()    
for x in text: 
    if x.lower() in "aáeéoóöőuúüű":
        break
    print(x, end=", ")    