package models
class User(userName: String, password: String){

  def toJsonString(): String ={
    "userName:" +this.userName +",password:"+ this.password
  }
}
