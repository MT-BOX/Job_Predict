// pages/message/message.js
var app=getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        selectcity:['全国','北京','上海','深圳','其它'],
        index1:0,
        selectedu:['不限学历','本科以下','本科','本科以上'],
        index2:0,
        jobname:'',
        jobexe:[],
        jobrif:null,
        city:'全国',
        edu:'',
        joblist:[],
        shows1: false,
        shows2: false
    },      
    // 点击下拉显示框
    selectTapscity() {
        this.setData({
          shows1: !this.data.shows1,
        });
      },
      // 点击下拉列表
      optioncity(e) {
        let Indexs = e.currentTarget.dataset.index; //获取点击的下拉列表的下标
        this.setData({
          index1: Indexs,
          shows1: !this.data.shows1,
          city:e.currentTarget.dataset.city
        });
        console.log(this.data.count.city)
      },
      selectTapsedu() {
        this.setData({
          shows2: !this.data.shows2,
        });
      },
      // 点击下拉列表
      optionedu(e) {
        let Indexs = e.currentTarget.dataset.index; //获取点击的下拉列表的下标
        var ed=''
        if(e.currentTarget.dataset.edu!='不限学历'){
          ed='-'+e.currentTarget.dataset.edu
        }
        this.setData({
          index2: Indexs,
          shows2: !this.data.shows2,
          edu:ed
        });
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
            jobname:app.globalData.job
        });
        console.log(this.data.jobname)
        wx.request({
            url: 'http://127.0.0.1:8000/api/getmessage/',
            method: 'POST',
            data:{
                skill:app.globalData.skills,
                jobname:this.data.jobname,
                education:app.globalData.accountInfo.education,
                welfare:[]
            },
            header: {
                'content-type': 'application/x-www-form-urlencoded' // 默认值
            },
            success:(res)=> {
                console.log(res.data);
                that.setData({
                    jobrif:res.data.job_bri,
                    joblist:res.data.joblist,
                    jobexe:res.data.jobexe
                });
            }
        })
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