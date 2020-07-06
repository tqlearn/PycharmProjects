// 获取当前日期“年/月/日”
pm.environment.set("now",new Date().toLocaleDateString());

// 用户秘钥
var secret_key = "475de36de482e9a2da9813dc2bd91a0d";
// 用户参数
var param = {
	"app_id" : "88a781ea",
	"room_id" : "lss_7b7be1bf"
}
var result = secret_key
for(var key in param){
    result=result+key+param[key]
}
result = result+secret_key

// 拼接出来的字符串就是
var md5=CryptoJS.MD5(result).toString();
pm.environment.set("md5", md5);