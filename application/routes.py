from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

# Step 1: 心の反応を学ぶ！
@main.route('/step1')
def step1():
    return render_template('step1/index.html')

@main.route('/step1/content/<topic>')
def step1_content(topic):
    return render_template(f'step1/{topic}.html')

@main.route('/step1/test')
def step1_test():
    return render_template('step1/test.html')

@main.route('/step1/test', methods=['POST'])
def step1_test_submit():
    # テスト結果の処理
    score = calculate_test_score(request.form, 'step1')
    flash(f'Step 1 テスト結果: {score}点')
    return redirect(url_for('main.step1_result', score=score))

@main.route('/step1/result')
def step1_result():
    score = request.args.get('score', default=0, type=int)
    return render_template('step1/result.html', score=score)

# Step 2: できていることを見つける！
@main.route('/step2')
def step2():
    return render_template('step2/index.html')

@main.route('/step2/content/<topic>')
def step2_content(topic):
    return render_template(f'step2/{topic}.html')

@main.route('/step2/test')
def step2_test():
    return render_template('step2/test.html')

@main.route('/step2/test', methods=['POST'])
def step2_test_submit():
    score = calculate_test_score(request.form, 'step2')
    flash(f'Step 2 テスト結果: {score}点')
    return redirect(url_for('main.step2_result', score=score))

@main.route('/step2/result')
def step2_result():
    score = request.args.get('score', default=0, type=int)
    return render_template('step2/result.html', score=score)

# Step 3: 何か違うことをやってみる！
@main.route('/step3')
def step3():
    return render_template('step3/index.html')

@main.route('/step3/content/<topic>')
def step3_content(topic):
    return render_template(f'step3/{topic}.html')

@main.route('/step3/test')
def step3_test():
    return render_template('step3/test.html')

@main.route('/step3/test', methods=['POST'])
def step3_test_submit():
    score = calculate_test_score(request.form, 'step3')
    flash(f'Step 3 テスト結果: {score}点')
    return redirect(url_for('main.step3_result', score=score))

@main.route('/step3/result')
def step3_result():
    score = request.args.get('score', default=0, type=int)
    return render_template('step3/result.html', score=score)

def calculate_test_score(form_data, step):
    """テストのスコアを計算する関数"""
    correct_answers = {
        'step1': {
            'q1': 'false',   # 災害後には身体面への影響もある
            'q2': 'false',   # 子どもを無理に元の状態に戻さない
            'q3': 'true',  # 回避や過覚醒が生じる
            'q4': 'true'    # 喪の作業は悲しみを抱きながら生活すること
        },
        'step2': {
            'q1': 'true',   # 小さな変化も進歩として捉える
            'q2': 'true',   # 自然回復では「できていること」を大切にする
            'q3': 'true'    # 例外探しは少し良かった時の要因を探す
        },
        'step3': {
            'q1': 'false',   # 個人によって適切な対処は異なる
            'q2': 'true',   # 吐く時間を長くする
            'q3': 'false',   # 筋弛緩法は力を入れて抜く
            'q4': 'true'    # 症状が長く続く場合には相談する
        }
    }
    
    total_questions = len(correct_answers[step])
    correct_count = 0
    
    for question, correct_answer in correct_answers[step].items():
        if form_data.get(question) == correct_answer:
            correct_count += 1
    
    return int((correct_count / total_questions) * 100)