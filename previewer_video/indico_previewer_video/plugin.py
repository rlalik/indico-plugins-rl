# Copyright (c) 2017 Rafal Lalik (rafallalik@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

import mimetypes

from flask import render_template

from indico.core import signals
from indico.core.plugins import IndicoPlugin
from indico.modules.attachments.preview import Previewer


class VideoPreviewer(Previewer):
    # All supported MIME types
    MIMETYPES = ( 'video/mp4', 'video/ogg', 'video/webm' )

    @classmethod
    def can_preview(cls, attachment_file):
        return attachment_file.content_type in cls.MIMETYPES

    @classmethod
    def generate_content(cls, attachment):
        return render_template('previewer_video:video_preview.html',
                               attachment=attachment)


class VideoPreviewerPlugin(IndicoPlugin):
    configurable = False

    def init(self):
        super(VideoPreviewerPlugin, self).init()
        self.connect(signals.attachments.get_file_previewers, self._get_file_previewers)

    def _get_file_previewers(self, sender, **kwargs):
        yield VideoPreviewer
