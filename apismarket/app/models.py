from app import db

class Selling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #판매 고유번호
    
    subject = db.Column(db.String(200), nullable=False)
    #판매 제목
    
    content = db.Column(db.Text(), nullable=False)
    #판매 내용
    
    create_date = db.Column(db.DateTime(), nullable=False)
    #작성 일시
    
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #답변 데이터의 고유 번호
    
    Selling_id = db.Column(db.Integer, db.ForeignKey('Selling.id', ondelete='CASCADE'))
    #판매 데이터의 고유 번호 
    
    Selling = db.relationship('Selling', backref=db.backref('answer_set'))
    #참조할 질문 모델
    
    content = db.Column(db.Text(), nullable=False)
    #대답 내용
    
    create_date = db.Column(db.DateTime(), nullable=False)
    #작성 일시
