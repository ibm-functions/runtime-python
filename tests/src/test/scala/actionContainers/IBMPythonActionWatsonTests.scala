/*
 * Copyright 2023 IBM Corporation
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
package actionContainers

import common.{TestHelpers, WskActorSystem, WskProps, WskTestHelpers}
import common.rest.WskRestOperations
import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import java.io.File
import spray.json._
import spray.json.DefaultJsonProtocol._

@RunWith(classOf[JUnitRunner])
class IBMPythonActionWatsonTests extends TestHelpers with WskTestHelpers with WskActorSystem {

  lazy val defaultKind = Some("python:3.6")

  implicit val wskprops: WskProps = WskProps()
  val wsk = new WskRestOperations
  val datdir = "tests/dat/watson/"
  val actionName = "testWatsonSDK"
  lazy val actionFileName = "testWatsonSDK.py"

  it should "Test whether or not watson package is usable within a python action" in withAssetCleaner(wskprops) {
    (wp, assetHelper) =>
      /*
     Disclaimer : Does not Use / Connect to a watson service! Tests that the
     watson-developer-cloud npm package is useable by verifying creating a new
     discover object creates the expected object with the expected properties.
       */

      val file = Some(new File(datdir, actionFileName).toString())

      assetHelper.withCleaner(wsk.action, actionName) { (action, _) =>
        action.create(
          actionName,
          file,
          main = Some("main"),
          kind = defaultKind,
          parameters = Map("hostname" -> wskprops.apihost.toJson))
      }

      withActivation(wsk.activation, wsk.action.invoke(actionName)) { activation =>
        val response = activation.response
        response.result.get.fields.get("error") shouldBe empty
        response.result.get.fields.get("load_successful") should equal(Some(JsBoolean(true)))
      }

  }
}
