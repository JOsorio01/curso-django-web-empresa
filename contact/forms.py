from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': "Nombre",
        }
    ), max_length=100)
    email = forms.EmailField(label="E-mail", required=True, widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': "E-mail",
        }
    ), min_length=5, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'rows': 3,
            'placeholder': "Escribe tu mensaje",
        }
    ), max_length=800)