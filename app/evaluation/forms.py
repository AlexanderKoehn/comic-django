from crispy_forms.helper import FormHelper
from django import forms

from evaluation.models import Method, Submission
from evaluation.validators import ExtensionValidator
from jqfileupload.widgets import uploader
from jqfileupload.widgets.uploader import UploadedAjaxFileList

method_upload_widget = uploader.AjaxUploadWidget(
    ajax_target_path="ajax/method-upload/",
    multifile=False)


class MethodForm(forms.ModelForm):
    chunked_upload = UploadedAjaxFileList(
        widget=method_upload_widget,
        label='Evaluation Method Container',
        validators=[
            ExtensionValidator(
                allowed_extensions=(
                    '.tar',
                )
            ),
        ],
        help_text=(
            'Tar archive of the container image produced from the command '
            '`docker save IMAGE > IMAGE.tar`. See '
            'https://docs.docker.com/engine/reference/commandline/save/'
        ),
    )

    def __init__(self, *args, **kwargs):
        super(MethodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Method
        fields = ['chunked_upload']


submission_upload_widget = uploader.AjaxUploadWidget(
    ajax_target_path="ajax/submission-upload/",
    multifile=False,
)


class SubmissionForm(forms.ModelForm):
    chunked_upload = UploadedAjaxFileList(
        widget=submission_upload_widget,
        label='Predictions File',
        validators=[
            ExtensionValidator(allowed_extensions=('.zip',))
        ],
    )

    def __init__(self, *args, **kwargs):
        """
        Conditionally render the comment field based on the
        display_comment_field kwarg
        """

        display_comment_field = kwargs.get('display_comment_field', False)
        if 'display_comment_field' in kwargs:
            del kwargs['display_comment_field']

        allow_supplementary_file = kwargs.get('allow_supplementary_file', False)
        if 'allow_supplementary_file' in kwargs:
            del kwargs['allow_supplementary_file']

        require_supplementary_file = kwargs.get('require_supplementary_file',
                                                False)
        if 'require_supplementary_file' in kwargs:
            del kwargs['require_supplementary_file']

        supplementary_file_label = kwargs.get('supplementary_file_label', '')
        if 'supplementary_file_label' in kwargs:
            del kwargs['supplementary_file_label']

        supplementary_file_help_text = kwargs.get(
            'supplementary_file_help_text', '')
        if 'supplementary_file_help_text' in kwargs:
            del kwargs['supplementary_file_help_text']

        super(SubmissionForm, self).__init__(*args, **kwargs)

        if not display_comment_field:
            del self.fields['comment']

        if supplementary_file_label:
            self.fields['supplementary_file'].label = supplementary_file_label

        if supplementary_file_help_text:
            self.fields[
                'supplementary_file'].help_text = supplementary_file_help_text

        if require_supplementary_file:
            self.fields['supplementary_file'].required = True
        elif not allow_supplementary_file:
            del self.fields['supplementary_file']

        self.helper = FormHelper(self)

    class Meta:
        model = Submission
        fields = (
            'comment',
            'supplementary_file',
            'chunked_upload',
        )