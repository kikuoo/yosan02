from yosan_app import db
from datetime import datetime


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)  # システムで使う番号
    name = db.Column(db.String(255))  # 工事名
    cord  = db.Column(db.Integer,default=0)  # 工事コード
    # is_remote = db.Column(db.Boolean)  
    ukeoi = db.Column(db.Integer,default=0)  # 請負金額
    jikko = db.Column(db.Integer, default=0)  # 実行予算
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時
