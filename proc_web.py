import random
from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar
import threading
import socket

app = Flask(__name__, static_folder="templates")


class proc_socket_client:
    proc_cpu = 0
    proc_men = 0
    proc_swap = 0
    proc_upnet = 0
    proc_dowmnet = 0

    def __init__(self):
        super().__init__()

    def socket_client(self):
        data = 0
        print("pc线程运行")
        # 创建一个socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.3.218', 7215))

        while True:

            if data == b'quit':
                print(b'connect quit.')
                break
            else:
                rec_data = client.recv(1024)
                print(rec_data)

                proc_data = rec_data.decode('UTF-8').split(',')
                print(proc_data)
                proc_socket_client.proc_cpu = eval(proc_data[0])
                proc_socket_client.proc_men = eval(proc_data[1])
                proc_socket_client.proc_swap = eval(proc_data[2])
                proc_socket_client.proc_upnet = eval(proc_data[3])
                proc_socket_client.proc_dowmnet = eval(proc_data[4])


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["cpu利用率", "men占用率", "swap占用率", "上传速度(KB)", "下载速度(KB))"])
        .add_yaxis("ubuntu-proc",
                   [proc_socket_client.proc_cpu, proc_socket_client.proc_men, proc_socket_client.proc_swap,
                    proc_socket_client.proc_upnet, proc_socket_client.proc_dowmnet])
        # .add_yaxis("android-proc", [random.randint(10, 100) for _ in range(5)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Linux_proc-系统监测"))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    threading.Thread(target=proc_socket_client().socket_client).start()
    app.run(threaded=True)

