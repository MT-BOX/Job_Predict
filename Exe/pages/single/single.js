// pages/single/single.js
var app=getApp()
Page({
 
    /**
     * 页面的初始数据
     */
    data: {
      // onPullDownRefresh: function () {
      //   wx.stopPullDownRefresh()
      // },
      myinfo:{
           phone:'15705625210',
           name:'马佳星',
           sex:'男',
           age:'21',
           education:'本科',
           job:'算法工程师',
           email:'2973614162@qq.com',
           key:'mjxmjc20010310',
      }
    },
   
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
      var stu = wx.getStorageSync('student');
      this.setData({ myinfo: stu });
      // console.log(this.data.myinfo);
    },
    exit:function(e){
      wx.showModal({
        title: '提示',
        content: '是否确认退出',
        success: function (res) {
          if (res.confirm) {
            // console.log('用户点击确定')
            wx.removeStorageSync('student');
            //页面跳转
            wx.redirectTo({
              url: '../Login/Login',
            })
          } else if (res.cancel) {
            console.log('用户点击取消')
          }
        }
      })
    },
    resetpwd:function(e){
      wx.navigateTo({
        url: '../ckey/ckey',
      })
    },
    correct:function(e){
        var no=this.data.myinfo.account;
        wx.navigateTo({
          url: '../correct/correct',
        })
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
      console.log(app.globalData.accountInfo)
      this.setData({
       myinfo:app.globalData.accountInfo
      })
      if(app.globalData.accountInfo.education==''){
        wx.showToast({
          title: "录入账号资料",
          icon: 'loading',
          duration: 1500
        });
        setTimeout(function(){
          wx.navigateTo({
            url: '../correct/correct',
          })
        },1500)
      }
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