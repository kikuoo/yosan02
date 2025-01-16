from flask import render_template,request,redirect,url_for
from yosan_app import db
from yosan_app.models.employee import Employee
from yosan_app import app

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('yosan_app/add_employee.html')
    if request.method == 'POST':
        form_name = request.form.get('name')
        form_mail = request.form.get('mail')
        form_is_remote = request.form.get('is_remote', default=False, type=bool)
        form_department = request.form.get('department')
        form_year = request.form.get('year', default=0, type=int)

        employee = Employee(
            name=form_name,
            mail=form_mail,
            is_remote=form_is_remote,
            department=form_department,
            year=form_year
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('employee_list'))


@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('yosan_app/employee_list.html', employees=employees)


@app.route('/employees/<int:id>')
def employee_detail(id):
    employee = Employee.query.get(id)
    # employee = Employee.query.get_or_404(id)
    # employee = Employee.query.filter(Employee.id == id).one()
    return render_template('yosan_app/employee_detail.html', employee=employee)


@app.route('/employees/<int:id>/edit', methods=['GET'])
def employee_edit(id):
    # 編集ページ表示用
    employee = Employee.query.get(id)
    return render_template('yosan_app/employee_edit.html', employee=employee)


@app.route('/employees/<int:id>/update', methods=['POST'])
def employee_update(id):
    employee = Employee.query.get(id)
    employee.name = request.form.get('name')
    employee.mail = request.form.get('mail')
    employee.is_remote = request.form.get('is_remote', default=False, type=bool)
    employee.department = request.form.get('department')
    employee.year = request.form.get('year', default=0, type=int)

    db.session.merge(employee)
    db.session.commit()
    return redirect(url_for('employee_list'))


@app.route('/employees/<int:id>/delete', methods=['POST'])
def employee_delete(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('employee_list'))

