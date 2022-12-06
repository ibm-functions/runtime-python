/*
 * Copyright 2017 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package integration

import common.{TestHelpers, WhiskProperties, WskActorSystem, WskProps, WskTestHelpers}
import common.rest.WskRestOperations
import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import java.io.File
import scala.io.Source
import spray.json._

@RunWith(classOf[JUnitRunner])
class CredentialsIBMPythonCloudantTests extends TestHelpers with WskTestHelpers with WskActorSystem {

  lazy val defaultKind = Some("python:3.7")
  lazy val actionFileName = "testCloudantService.py"

  implicit val wskprops: WskProps = WskProps()
  val wsk = new WskRestOperations
  val datdir = "tests/dat/cloudant/"

  // read credentials from from vcap_services.json
  val vcapFile = WhiskProperties.getProperty("vcap.services.file")
  val vcapString = Source.fromFile(vcapFile).getLines.mkString
  val vcapInfo =
    JsonParser(ParserInput(vcapString)).asJsObject.fields("cloudantNoSQLDB").asInstanceOf[JsArray].elements(0)
  val creds = vcapInfo.asJsObject.fields("credentials").asJsObject
  val username = creds.fields("username").asInstanceOf[JsString]
  val password = creds.fields("password").asInstanceOf[JsString]
  val host = creds.fields("host").asInstanceOf[JsString]

  val actionName = "testCloudantService"

  it should "Test whether or not cloudant database is reachable using cloudant python package" in withAssetCleaner(
    wskprops) { (wp, assetHelper) =>
    val file = Some(new File(datdir, actionFileName).toString())

    assetHelper.withCleaner(wsk.action, actionName) { (action, _) =>
      action.create(
        actionName,
        file,
        main = Some("main"),
        kind = defaultKind,
        parameters = Map("username" -> username, "password" -> password, "host" -> host))
    }

    withActivation(wsk.activation, wsk.action.invoke(actionName)) { activation =>
      val response = activation.response
      response.result.get.fields.get("error") shouldBe empty
      response.result.get.fields.get("lastname") should be(Some(JsString("Queue")))
    }

  }

}
