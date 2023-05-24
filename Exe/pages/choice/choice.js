// pages/choice/choice.js
var app=getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        activityset: [
        ],
      },
      /**
       * 生命周期函数--监听页面加载
       */
      onLoad: function (options) {
      },
      seletvalue: function (e) {
        var that = this;
        var curindex = e.currentTarget.id;
        console.log(that.data.activityset)
        var activityset = that.data.activityset;
        if (that.data.activityset[curindex].selected==null){
          that.data.activityset[curindex].selected = [];
        }  //当activityset中没有selected时，添加并定义成数组用于后面push数据进去
        var selected = that.data.activityset[curindex].selected;
        console.log(selected);   
        var values = e.currentTarget.dataset.name;
        selected.push(values);  //往selected数组中添加数据
         console.log(selected);
        that.data.activityset[curindex]["select" + [e.currentTarget.dataset.idx]]= values;  //往当前index的json数据中添加select＋目前下标数字的数据，用于前端判断是否有该数据
        that.setData({
          activityset: activityset
        })
      },
      deletvalue: function (e) {
        var that = this;
        var activityset = that.data.activityset;
        var curindex = e.currentTarget.id;
        console.log(that.data.activityset);
        delete that.data.activityset[curindex]["select" + [e.currentTarget.dataset.idx]];
        var selected = that.data.activityset[curindex].selected;
        var values = e.currentTarget.dataset.name;
        var indexnow = (selected || []).findIndex((item) => item === values);  //这个用来获取需要删除的数据在数组中的下标
        selected.splice(indexnow, 1);  //这个用来删除从下标开始对应数量的数据
        console.log(selected);
        that.setData({
          activityset: activityset
        })
      },
    predict:function(){
          var skill=[];
          var ss=this.data.activityset;
          var lens=ss.length;
          var i=0;
          while(i<lens){
              for(var j=0;j < (ss[i].selected.length);j++){
                  skill.push(ss[i].selected[j])
                }
              i++;
          }
          console.log(skill);
          app.insitskill(skill)
          
          wx.showToast({
            title: "预测成功",
            icon: 'success',
            duration: 2000
          });
          setTimeout(
            function(){ //注意function这里不能缺少
              wx.navigateBack({
                delta:1,
              })
            },2000)
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
    onShow(){
        let that =this;
        wx.request({
            url: 'http://127.0.0.1:8000/api/getskill/',
            method: 'POST',
            data:{
                da:12
            },
            header: {
              'content-type': 'application/x-www-form-urlencoded' // 默认值
            },
            success:(res)=> {
              console.log(res.data)
              this.setData({
                activityset:res.data.skill
              })
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