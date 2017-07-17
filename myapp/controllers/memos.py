from myapp.controllers import *
from flask_wtf import Form
from wtforms import validators
from wtforms.fields import TextField, TextAreaField
from wtforms.validators import Required
from myapp.models import Memo, Tag, MemoTag
from flask import g
from myapp.valiables.hoge import hoge
from myapp.controllers.general_base import GeneralBaseView


class MemosView(GeneralBaseView):

    route_base='/'
    per_page = 8

    def before_request(self, name, **view_args):
        return super().before_request(name, **view_args)

    @route('/memos/', defaults={'page': 1})
    @route('/memos/page/<int:page>')
    def index(self, page):
        memos = Memo.query.filter(Memo.user_id == self.current_user.id).order_by(Memo.id.desc()).paginate(page, self.per_page)
        return render_template('memos/index.html', memos=memos)

    @route('/memos/<int:id>/show')
    def show(self, id):
        memo = Memo.query.get(id)
        memo.make_tag_str()
        return render_template('memos/show.html', memo=memo)

    @route('/memos/new')
    def new(self):
        form = Registration()
        return render_template('memos/new.html', form=form)

    @route('/memos/<int:id>/edit')
    def edit(self, id):
        memo = Memo.query.get(id)
        memo.make_tag_str()
        form = Registration(obj=memo)
        return render_template('memos/edit.html', form=form, memo=memo)

    @route('/memos/create', methods=['POST'])
    def create(self):
        form = Registration(request.form)
        if form.validate():
            memo = Memo(title=form.title.data,content=form.content.data,user_id=self.current_user.id)
            memo.append_tags(form.tag_str.data)
            db.session.add(memo)
            db.session.commit()
            flash('The memo was created.')
            return redirect('/memos/' + str(memo.id) + '/edit')
        return render_template('memos/new.html', form=form)


    @route('/memos/<int:id>/update', methods=['POST'])
    def update(self,id):
        memo = Memo.query.filter_by(id=id).first()
        form = Registration(request.form)
        old_tag_ids = MemoTag.query.filter_by(memo_id=id)
        if form.validate():
            old_tag_ids.delete()
            memo.append_tags(form.tag_str.data)
            memo.title = form.title.data
            memo.content = form.content.data
            memo.user_id = self.current_user.id
            db.session.commit()
            flash('The memo was edited.')
            return redirect('/memos/' + str(memo.id) + '/edit')
        return render_template('memos/new.html', form=form)


    @route('/memos/<int:id>/destroy', methods=['POST'])
    def destroy(self,id):
       db.session.delete(Memo.query.filter_by(id=id).first())
       db.session.commit()
       flash('The memo was deleted.')
       return redirect('/memos/')


class Registration(Form):
    title = TextField('Title',
        [validators.Length(min=4, message='You should input with 4 characters or more.')],
        render_kw={"placeholder": "Title"}
    )
    content = TextAreaField('Content',
        [validators.Required(message='This is required.')],
        render_kw={"placeholder": "Content"}
    )
    tag_str = TextField('Tag',
        render_kw={"placeholder": "Tag. Please input it separated by commas."}
    )
