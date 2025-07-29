// 保存原始方法
const originalParse = JSON.parse;

// 覆盖 JSON.parse
JSON.parse = function(text, reviver) {
    debugger ;const result = originalParse.apply(this, [text, reviver]);console.log(JSON.stringify(result));
    return result;
};