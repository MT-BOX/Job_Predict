//Login.js
//获取应用实例
var app = getApp()
 
Page({
  data: {
    username: '',
    password: ''
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onShow: function () {
  },
  onLoad: function () {
  },
 
 
  // 获取输入账号 
  bindusername: function (e) {
    this.setData({
      username: e.detail.value
    });
  },
 
  // 获取输入密码 
  bindpassword: function (e) {
    this.setData({
      password: e.detail.value
    });
  },
 
  // 登录处理
  login: function () {
    // wx.switchTab({
    //   url: '../home/home',
    // })
    // console.log(this.data.username,this.data.password)
    console.log(this.data)
    var that = this;
    if (this.data.username.length == 0 || this.data.password.length == 0) {
      wx.showToast({
        title: '账号或密码不能为空',
        icon: 'none',
        duration: 2000
      })
    } else {
      wx.request({
        url: 'http://127.0.0.1:8000/api/login/', // 仅为示例，并非真实的接口地址
        method: 'POST',
        data: {
          username: that.data.username,
          password: that.data.password
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        success(res) {
          console.log(res.data)
          if (res.data.isok==1) {
            res.data.account.phone=that.data.username
            app.insitcinfo(res.data.account);
            app.insitresult([]);
            console.log(app.globalData.predictresult)
            wx.switchTab({
              url: '../single/single',
            })
          } else if(res.data.isok==2){
            wx.showModal({
              title: '账号不存在',
              content: '是否使用当前账号和密码新建用户',
              success: function (s) {
                if (s.confirm) {
                  // console.log('用户点击确定')
                  wx.request({
                    url: 'http://127.0.0.1:8000/api/creat/', 
                    method: 'POST',
                    data: {
                      username: that.data.username,
                      password: that.data.password
                    },
                    header: {
                      'content-type': 'application/x-www-form-urlencoded' // 默认值
                    },
                    success(news){
                        //页面跳转
                        app.insitcinfo(news.data.account);
                        app.insitresult([]);
                        wx.switchTab({
                          url: '../single/single',
                        })
                    }
                  })
                } else if (res.cancel) {
                  console.log('用户点击取消')
                }
              }
            })
          }
          else{
            wx.showToast({
              title: "密码错误",
              icon: 'none',
              duration: 2000
            })
          }
        }
      })
    }
  }
})