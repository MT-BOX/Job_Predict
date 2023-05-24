// pages/home/home.js

var app=getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
          jobresult:[],
          skill:[],
          isok:false
    },
    collect:function(){
        wx.navigateTo({
            url: '../choice/choice',
          })
    },
    getmessage:function(e){
        var jobname = e.currentTarget.dataset.name
        app.insitjob(jobname)
        wx.navigateTo({
            url: '../message/message'
        })
    },

    getRings(){
      this.data.jobresult.forEach((item,index)=>{
        this.canvasRing = this.selectComponent("#can"+index);
        this.canvasRing.drawCanvasRing()
      })
    },
    drawNew(step){
      const query = wx.createSelectorQuery().in(this);
      query.select('#myCanvas')
        .fields({ node: true , size: true})
        .exec(this.init.bind(this))
    },
    init(res){
      const canvas = res[0].node
      const ctx = canvas.getContext('2d');
      const dpr = wx.getSystemInfoSync().pixelRatio
      canvas.width = res[0].width * dpr
      canvas.height = res[0].height * dpr
      ctx.scale(dpr, dpr)
      var gradient = ctx.createLinearGradient(200, 100, 100, 200);
      gradient.addColorStop("0", "#a57b5f");
      gradient.addColorStop("0.5", "#cc9ad1");
      gradient.addColorStop("1.0", "#b84e88");
      ctx.strokeStyle=gradient;
      ctx.lineWidth=10;
      ctx.lineCap='round';
      ctx.beginPath(); 
      ctx.arc(110, 110, 100, 0, 2 * Math.PI, false);
      ctx.stroke(); 
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
         let that=this;
         this.setData({
           jobresult:[],
           isok:true
         })
         this.data.skill=app.globalData.accountInfo.skill
         console.log(this.data.skill)
         if(this.data.skill.length!=0){
          this.setData({
            isok:false
          })

            wx.request({
                url: 'http://127.0.0.1:8000/api/predict/',
                method: 'POST',
                data:{
                    account:app.globalData.accountInfo.phone,
                    skills:this.data.skill
                },
                header: {
                  'content-type': 'application/x-www-form-urlencoded' // 默认值
                },
                success:(res)=> {
                  console.log(res.data);
                  that.setData({
                      jobresult:res.data.result
                  });
                  app.insitresult(res.data.result)
                }
            })
         }
         console.log(this.data.jobresult)

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})