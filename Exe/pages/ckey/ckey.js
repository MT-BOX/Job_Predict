// pages/ckey/ckey.js

var app=getApp()
Page({
    /**
     * 页面的初始数据
     */
    data: {
          oldkey:'',
          newkey:'',
          setkey:'',
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
        this.setData({
           oldkey:'',
           newkey:'',
           setkey:''
        })
    },
        /**
     * 输入旧密码
     */
    setold:function(e){
        this.setData({
            oldkey:e.detail.value
        })
    },
            /**
     * 输入旧密码
     */
    setnew:function(e){
        this.setData({
            newkey:e.detail.value
        })
    },
            /**
     * 输入旧密码
     */
    setset:function(e){
        this.setData({
            setkey:e.detail.value
        })
    },
    correctkey:function(){
        var aco=app.globalData.accountInfo;
        console.log(aco)
        if(aco.key!=this.data.oldkey){
            wx.showToast({
                title: "原始密码错误",
                icon: 'none',
                duration: 2000
              })
        }
        else if(this.data.setkey!=this.data.newkey){
            wx.showToast({
                title: "确认密码不匹配",
                icon: 'none',
                duration: 2000
              })
        }
        else{
            aco.key=this.data.newkey;
            app.insitcinfo(aco);
            wx.request({
                url: 'http://127.0.0.1:8000/api/ckey/', // 仅为示例，并非真实的接口地址
                method: 'POST',
                data: {
                  username: aco.phone,
                  password: this.data.newkey
                },
                header: {
                  'content-type': 'application/x-www-form-urlencoded' // 默认值
                },
                success(res){
                     if(res.data.isok);
                     wx.showToast({
                        title: "密码修改成功",
                        icon: 'success',
                        duration: 2000
                      });
                      setTimeout(
                        function(){ //注意function这里不能缺少
                          wx.navigateBack({
                            delta: 1,
                          })
                        },2000)
                }
            })
        }
    }
})