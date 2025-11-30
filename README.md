## 项目简介

本项目用于南京大学宿舍电费查询，基于 Flask 提供 Web API，支持 Docker 部署。

## Docker 部署方法

1. 构建镜像：
	```shell
	docker build -t nju-power-monitor .
	```

2. 运行容器（可通过环境变量配置参数）：
	```shell
	docker run -d -p 5000:5000 \
	  -e BUI_ID=gl11 \
	  -e BUI_NAME="11舍" \
	  -e FLOOR_ID=002 \
	  -e FLOOR_NAME="第2层" \
	  -e ROOM_NAME="204房间" \
	  -e ROOM_ID=1111 \
	  --name nju-power-monitor nju-power-monitor
	```

## 参数说明

所有参数均可通过环境变量设置，也可通过 GET 请求参数传递：

- `BUI_ID`：楼栋ID，默认 gl11
- `BUI_NAME`：楼栋名称，默认 11舍
- `FLOOR_ID`：楼层ID，默认 002
- `FLOOR_NAME`：楼层名称，默认 第2层
- `ROOM_NAME`：房间名称，默认 204房间
- `ROOM_ID`：房间ID，默认 1111
- `PORT`：服务端口，默认 5000

## API 使用

访问 `http://<服务器IP>:5000/power` 即可获取剩余电量，支持通过 URL 参数动态查询。

示例：
```
http://localhost:5000/?bui_id=gl11&bui_name=11舍&floor_id=002&floor_name=第2层&room_name=204房间&room_id=1111
```
# NJU宿舍电费监控系统
由于宿舍搭建的NAS面临宿舍电费耗尽停电危险, 但南大APP上查看电费过于复杂~~和不够酷~~, 希望能有一个快捷的电费监控和预警系统, 帮助查看电费剩余情况, 避免断电, ~~节省UPS的开销~~

## 思路

思路来自<https://github.com/GeRongcun/NJU_MonitorElectricityCosts>


学校有个网址(内网访问)可以查询电表余量
- 仙林校区<http://172.27.2.95:8899/query/>
- 鼓楼校区<http://114.212.254.14:8899/query/>

本项目采用 requests 库直接获取电费数据，无需浏览器自动化。

## 后续开发
- [x] 支持 requests 直接获取电费数据
- [x] 参数化配置房间地址和校区
- [x] 部署为 flask服务，方便在 NAS 上搭建，集成到 Home Assistant
