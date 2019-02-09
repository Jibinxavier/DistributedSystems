package controllers

import javax.inject.{Inject, Singleton}
import models.{User, UserObj}
import play.api.mvc.{AbstractController, ControllerComponents, Request}
import play.api.libs.json._
import akka.actor.ActorSystem

// you need this import to have combinators
import play.api.libs.functional.syntax._

class AuthenticationController @Inject()(cc: ControllerComponents,   userDao: UserObj) extends AbstractController(cc) {


  def signUp = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map{
        case (userName, password) =>
          Ok(userDao.signup( new User(userName, password)))
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toFlatJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }


  def login = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map{
        case (userName, password) =>
          Ok(userDao.signup( new User(userName, password)))
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toFlatJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }

}
