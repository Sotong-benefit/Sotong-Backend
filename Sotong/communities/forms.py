from django import forms
from .models import Community

class CommunityBaseForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"

class CommunityCreateForm(CommunityBaseForm):
    # description = forms.CharField(widget=forms.Textarea)
    class Meta(CommunityBaseForm.Meta):
        fields = ['image', 'description' , 'title', 'tags', 'file']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 각 필드에 placeholder를 추가합니다.
        self.fields['title'].widget.attrs['placeholder'] = '제목을 입력해주세요.'
        self.fields['tags'].widget.attrs['placeholder'] = '태그를 입력해주세요'
        self.fields['description'].widget.attrs['placeholder'] = '게시글을 작성하세요'

        self.fields['title'].widget.attrs['id'] = 'postTitle'


        self.fields['image'].widget.attrs['class'] = 'media-button'
        self.fields['file'].widget.attrs['class'] = 'media-button'
        self.fields['tags'].widget.attrs['class'] = 'tag-input'

        self.fields['image'].widget.attrs['style'] = 'display:none'
        self.fields['file'].widget.attrs['style'] = 'display:none'



        