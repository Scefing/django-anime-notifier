import json

from django import forms
from .models import Show, Json


def str_to_bool(s):
    if s == 'true':
        return True
    elif s == 'false':
        return False


class JsonForm(forms.ModelForm):

    class Meta:
        model = Json
        exclude = []


class ShowForm(forms.ModelForm):

    class Meta:
        model = Show
        exclude = []


class JsonUploadForm(forms.Form):

    file = forms.FileField()

    def __init__(self):
        super().__init__()
        self.instances = []

    def convert_json(self):
        data = json.loads(self.file)

        show_list = data["items"]

        for entry in show_list:
            show = {"name": entry["name"],
                    "MALID": int(entry["MALID"]),
                    "ANNID": int(entry["ANNID"]),
                    "notes": entry["notes"],
                    "simulcast": entry["simulcast"],
                    "type": entry["type"],
                    "name_lower": entry["name_lower"],
                    "missing_airdate": str_to_bool(entry["missingAirdate"]),
                    "missing_airtime": str_to_bool(entry["missingAirtime"]),
                    "is_short" : str_to_bool(entry["isShort"]),
                    "commentary" : str_to_bool(entry["commentary"]),
                    "simulcast_delay_orig" : float(entry["simulcast_delay_orig"]),
                    "simulcast_delay" : str_to_bool(entry["simulcast_delay"]),
                    "simulcast_invalid" : str_to_bool(entry["simulcast_invalid"]),
                    "fansub" : str_to_bool(entry["fansub"]),
                    "has_translation" : str_to_bool(entry["hasTranslation"]),
                    "simulcast_class" : entry["simulcastClass"],
                    "fansub_class" : entry["fansubClass"],
                    "airdate_u" : int(entry["airdate_u"])
                    }

            if Show.get(**show):
                pass
            else:
                form = ShowForm(show)
                if form.is_valid():
                    saving = form.save(commit=False)
                    self.instances.append(saving)
                else:
                    raise forms.ValidationError(u"The file contains invalid data.")
        return data

    def save(self):
        instances = getattr(self, "instances", None)
        if instances:
            for entry in instances:
                entry.save()
        return instances