// app.js
App({
  globalData: {
    accountInfo: null,
    predictresult:[],
    job:null
  }
  ,
  onLaunch() {
  //云开发环境初始化
  wx.cloud.init({
    env:"zhike-0g3asztle60f83ad"
  })
  },
  insitcinfo:function(res){
     this.globalData.accountInfo=res
  },
  insitjob:function(res){
    this.globalData.job=res
 },
  insitskill:function(res){
    this.globalData.accountInfo.skill=res
 },
 insitresult:function(res){
  this.globalData.predictresult=res
}
})
