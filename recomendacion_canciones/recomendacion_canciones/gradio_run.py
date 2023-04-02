import gradio as gr
from typing import List
from .base_config import BaseConfig
from .models import Tracks
import jinja2

TEMPLATE = jinja2.Template("""
<html>
<title>Attributes</title>
<table>
    <tr>
        {% for column in cols %}
            <th>{{column}}</th>
        {% endfor %}
    </tr>
{% for row in attrs %}
    <tr>
        {% for column in row %}
            <td>{{column}}</td>
        {% endfor %}
    </tr>
{% endfor %}
</table>
</html>""")

class GradioRun():
    def __init__(self):
        self.base = BaseConfig()
        # consigue las primeras 20
        self.track_options = self.similar_tracks_name('')

        # GRADIO

        demo = gr.Blocks()
        with demo:
            with gr.Row():
                text_input = gr.Textbox(label="Search bar")
                search_tracks_btn = gr.Button("Match Closest tracks")

            with gr.Row():
                self.text_options = gr.Dropdown(
                    choices = self.get_str_options(),
                    # type = 'index',
                    label = "Closest 20 options",
                    multiselect = False
                )
                select_track_btn = gr.Button("Select track")

            recommendations = gr.HTML(
                label="Recommended tracks",
                interactive=False
            )
            search_tracks_btn.click(self.find_similar_tracks, inputs=text_input, outputs=self.text_options)
            select_track_btn.click(self.find_recommended_tracks, inputs=self.text_options, outputs=recommendations)

        demo.launch(debug=True)

    def get_str_options(self) -> List[str]:
        return list(map(lambda x: x.name, self.track_options))

    def similar_tracks_name(self, name):
        return Tracks.search_similar_name(name, 20)

    def find_similar_tracks(self, name):
        self.track_options = self.similar_tracks_name(name)
        return gr.Dropdown.update(choices=self.get_str_options())

    def find_recommended_tracks(self, value):
        if value:
            # por alguna razon text_options deja de funcionar correctamente en caso de actualizar la lista
            index = self.get_str_options().index(value)

            # print('dropdown:', index)
            track = self.track_options[index]
            # TODO: to html
            recs = self.base.get_recommendation_song(track.id)
            return TEMPLATE.render({'cols': [column.key for column in Tracks.__table__.columns],'attrs': recs})
        return ""
