#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message='请输入正确的邮箱! ')],
                        render_kw={'class': "form-control", "required": "required"},
                        _name="email"
                        )
    password = PasswordField(label='密码', validators=[DataRequired()],
                             render_kw={'class': "form-control", "required": "required"},
                             _name="password"
                             )
    remember_me = BooleanField(label='记住我')
    validate = StringField(u'验证码', validators=[DataRequired(message=u'验证码不能为空'),
                                               Regexp(r'^[a-zA-Z0-9][a-zA-Z0-9]*$', 0, u'验证码只能包含字母数字')],
                           render_kw={'class': "form-control", "required": "required"},
                           _name="validate"
                           )
    submit = SubmitField(render_kw={'class': "btn btn-info btn-block"})

    def get_user(self):
        from ..models import User
        return User.query.filter_by(email=self.data['email']).first()


class RegistForm(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired(),
                                                    Length(min=5, max=16, message='用户名必须大于5位! '),
                                                    Regexp(r'^[a-zA-Z0-9_][a-zA-Z0-9]*$', 0, u'用户名只能包含字母数字下划线')],
                           render_kw={'class': "form-control", "required": "required"},
                           _name="username"
                           )

    password = PasswordField(label='密码', validators=[DataRequired(),
                                                     Length(min=6, max=16, message='密码必须大于6位! '),
                                                     Regexp(r'^[a-zA-Z0-9_][a-zA-Z0-9]*$', 0, u'密码只能包含字母数字下划线')],
                             render_kw={'class': "form-control", "required": "required"},
                             _name="password"
                             )
    confirm = PasswordField(label='确认密码', validators=[DataRequired(), EqualTo('password', message='两次输入的密码不一样! ')],
                            render_kw={'class': "form-control", "required": "required"},
                            _name="qrpassword", )
    email = StringField(label='邮箱', validators=[DataRequired(), Email(message='请输入正确的邮箱! ')],
                        render_kw={'class': "form-control", "required": "required"},
                        _name="email"
                        )
    val = StringField(u'验证码', validators=[DataRequired(message=u'验证码不能为空'),
                                          Regexp(r'^[a-zA-Z0-9][a-zA-Z0-9]*$', 0, u'验证码只能包含字母数字')],
                      render_kw={'class': "form-control", "required": "required"},
                      _name="validate"
                      )
    submit = SubmitField(render_kw={'class': "btn btn-info btn-block"})

    def validate_username(self, field):
        from ..models import User
        data = field.data
        if User.query.filter_by(username=data).first():
            raise ValidationError('用户名已存在')
        return data

    def validate_email(self, field):
        from ..models import User
        data = field.data
        if User.query.filter_by(email=data).first():
            raise ValidationError('邮箱已存在')
        return data

    def validate_val(self, field):
        from flask import session
        data = field.data
        if 'code_text' in session and data.lower() != session['code_text'].lower():
            raise ValidationError('验证码错误')
        return data


class AuthEmail(FlaskForm):
    email = StringField('email', validators=[DataRequired("请输入您注册时使用的邮箱")],
                        render_kw={'class': "form-control", "required": "required"},
                        _name="email")

    val = StringField(u'验证码', validators=[DataRequired(message=u'验证码不能为空'),
                                          Regexp(r'^[a-zA-Z0-9][a-zA-Z0-9]*$', 0, u'验证码只能包含字母数字')],
                      render_kw={'class': "form-control", "required": "required"},
                      _name="validate"
                      )

    def get_user(self):
        from ..models import User
        return User.query.filter_by(email=self.data['email']).first()

    def validate_val(self, field):
        from flask import session
        data = field.data
        if 'code_text' in session and data.lower() != session['code_text'].lower():
            raise ValidationError('验证码错误')
        return data


class ResetPassword(FlaskForm):
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=16, message='密码必须大于6位! ')],
                             render_kw={'class': "form-control", "required": "required"})
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='两次输入的密码不一样! ')],
                            render_kw={'class': "form-control", "required": "required"})


class BindAccount(FlaskForm):
    email = StringField('email', validators=[DataRequired("请输入您要绑定的的邮箱")],
                        render_kw={'class': "form-control", "required": "required"})
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=16, message='密码必须大于6位! ')],
                             render_kw={'class': "form-control", "required": "required"})
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='两次输入的密码不一样! ')],
                            render_kw={'class': "form-control", "required": "required"})

    def validate_email(self, field):
        from ..models import User
        data = field.data
        if User.query.filter_by(email=data).first():
            raise ValidationError('邮箱已存在')
        return data
