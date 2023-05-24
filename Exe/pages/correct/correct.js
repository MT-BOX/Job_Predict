// pages/correct/correct.js

var app=getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        count:{
            name:'',
            age:'',
            sex:'男',
            email:'',
            education:'本科',
            skill:[],
            phone:''
        },
        shows: false, //控制下拉列表的显示隐藏，false隐藏、true显示
        selectDatas: ['中专', '大专', '本科','硕士','博士'], //下拉列表的数据
        indexs: 2, //选择的下拉列 表下标,
      },
    
      // 点击下拉显示框
      selectTaps() {
        this.setData({
          shows: !this.data.shows,
        });
      },
      // 点击下拉列表
      optionTaps(e) {
        let Indexs = e.currentTarget.dataset.index; //获取点击的下拉列表的下标
        this.setData({
          indexs: Indexs,
          shows: !this.data.shows
        });
        this.data.count.education=e.currentTarget.dataset.edu
        console.log(this.data.count.education)
      },
      getname:function(e){
        this.data.count.name=e.detail.value
      },
      getage:function(e){
        this.data.count.age=e.detail.value
      },
      getemail:function(e){
        this.data.count.email=e.detail.value
      },
      getsex:function(e){
        this.data.count.sex=e.detail.value
      },
      save:function(e){
          var cot=this.data;
          wx.request({
            url: 'http://127.0.0.1:8000/api/correct/', // 仅为示例，并非真实的接口地址
            method: 'POST',
            data: {
              name:cot.count.name,
              age:cot.count.age,
              sex:cot.count.sex,
              email:cot.count.email,
              education:cot.count.education,
              skill:cot.count.skill,
              phone:cot.count.phone
            },
            header: {
              'content-type': 'application/x-www-form-urlencoded' // 默认值
            },
            success(res) {
              if(res.data.isok){
                app.insitcinfo(cot.count);
                wx.showToast({
                  title: "资料修改成功",
                  icon: 'success',
                  duration: 2000
                });
                setTimeout(
                  function(){ //注意function这里不能缺少
                    wx.navigateBack({
                      delta:1,
                    })
                  },2000)
              }
            }
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
         this.setData({
           count:app.globalData.accountInfo
         });
         if(this.data.count.sex==''){
          this.data.count.sex='男'
         }
         if(this.data.count.education==''){
          this.data.count.education='本科'
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