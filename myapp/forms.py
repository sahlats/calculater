from django import forms

class BmiForm(forms.Form):
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

class EmiForm(forms.Form):
    amount=forms.IntegerField(label='loan amount',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    interest=forms.IntegerField(label='interest',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    tenure=forms.IntegerField(label='loan tenure',widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

class CalorieForm(forms.Form):
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    gender_choices=(
        ("male","male"),
        ("female","female")
    )
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
    activity_choices=(
        (1.2,"sedentary "),
        (1.375,"lightly active"),
        (1.55,"moderatly active"),
        (1.725,"very active"),
        ( 1.9,"extra active")
    )
    activity_level=forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))

class CalorieManageForm (CalorieForm):
    
    target_weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    
    duration=forms.IntegerField(label="duration in weeks", widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    weight_choices=(
        (1,"weight gain"), 
        (2, "weight loss")
        )
    weight_choices=forms.ChoiceField(choices=weight_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
        
