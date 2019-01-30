package controllers

import javax.inject.{Inject, Singleton}
import play.api.mvc.{AbstractController, ControllerComponents}
 
import play.api.libs.json._
// you need this import to have combinators
import play.api.libs.functional.syntax._

class AuthenticationController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {


  implicit val rds = (
    (__ \ 'name).read[String] and
      (__ \ 'age).read[Long]
    ) tupled
  def signUp = Action {

    Ok("Here's your sign up page")
  }

  def login =  Action {
    Ok("here is your login pager")
  }

}
