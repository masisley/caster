from dragonfly import *

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.lib.dfplus.additions import IntegerRefST

class KustoRule(MergeRule):
  pronunciation = "Kusto"

  mapping = {    
    "TIMESTAMP":            R(Text("TIMESTAMP"), rdescript="Kusto: TIMESTAMP"),
    "PreciseTimeStamp":     R(Text("PreciseTimeStamp"), rdescript="Kusto: PreciseTimeStamp"),
    "Deployment":           R(Text("Deployment"), rdescript="Kusto: Deployment"),
    "Role":                 R(Text("Role"), rdescript="Kusto: Role"),
    "RoleInstance":         R(Text("RoleInstance"), rdescript="Kusto: RoleInstance"),
    "Level":                R(Text("Level"), rdescript="Kusto: Level"),
    "Pid":                  R(Text("Pid"), rdescript="Kusto: Pid"),
    "Tid":                  R(Text("Tid"), rdescript="Kusto: Tid"),
    
    "Task Name":             R(Text("TaskName"), rdescript="Kusto: TaskName"),
    "Activity ID":           R(Text("ActivityId"), rdescript="Kusto: ActivityId"),
    "subscription ID":       R(Text("subscriptionId"), rdescript="Kusto: subscriptionId"),
    "correlation ID":        R(Text("correlationId"), rdescript="Kusto: correlationId"),
    "principal Oid":         R(Text("principalOid"), rdescript="Kusto: principalOid"),
    "principal Puid":        R(Text("principalPuid"), rdescript="Kusto: principalPuid"),
    "tenant ID":             R(Text("tenantId"), rdescript="Kusto: tenantId"),
    "authorization Source":  R(Text("authorizationSource"), rdescript="Kusto: authorizationSource"),
    "operation Name":        R(Text("operationName"), rdescript="Kusto: operationName"),
    "http Method":           R(Text("httpMethod"), rdescript="Kusto: httpMethod"),
    "host Name":             R(Text("hostName"), rdescript="Kusto: hostName"),
    "target URI ":            R(Text("targetUri"), rdescript="Kusto: targetUri"),
    "user Agent":            R(Text("userAgent"), rdescript="Kusto: userAgent"),
    "client Request ID":      R(Text("clientRequestId"), rdescript="Kusto: clientRequestId"),
    "client Session ID":      R(Text("clientSessionId"), rdescript="Kusto: clientSessionId"),
    "client Application ID":  R(Text("clientApplicationId"), rdescript="Kusto: clientApplicationId"),
    "content Length":        R(Text("contentLength"), rdescript="Kusto: contentLength"),
    "duration In Milliseconds":	  R(Text("durationInMilliseconds"), rdescript="Kusto: durationInMilliseconds"),
    "http Status Code":       R(Text("httpStatusCode"), rdescript="Kusto: httpStatusCode"),	#exceptionMessage	errorCode	failureCause	errorMessage	referer	commandName	parameterSetName	contentType	contentEncoding	SourceNamespace	SourceMoniker	SourceVersion	armServiceRequestId
    "Source Namespace":      R(Text("SourceNamespace"), rdescript="Kusto: SourceNamespace"),
    "workflow ID":      R(Text("workflowId"), rdescript="Kusto: workflowId"),
    "workflow Name":      R(Text("workflowName"), rdescript="Kusto: workflowName"),
    "flow Name":      R(Text("flowName"), rdescript="Kusto: flowName"),
    "flow Id":      R(Text("flowId"), rdescript="Kusto: flowId"),

    "ClientErrors":      R(Text("ClientErrors"), rdescript="Kusto: ClientErrors"),
    "ClientRequests":      R(Text("ClientRequests"), rdescript="Kusto: ClientRequests"),
    "ClientTelemetry":      R(Text("ClientTelemetry"), rdescript="Kusto: ClientTelemetry"),
    "ClientTraces":      R(Text("ClientTraces"), rdescript="Kusto: ClientTraces"),
    "Errors":      R(Text("ErrorsAll"), rdescript="Kusto: Errors"),
    "HttpIncomingRequests":      R(Text("HttpIncomingRequestsAll"), rdescript="Kusto: HttpIncomingRequests"),
    "HttpOutgoingRequests":      R(Text("HttpOutgoingRequestsAll"), rdescript="Kusto: HttpOutgoingRequests"),
    "JobErrors":      R(Text("JobErrors"), rdescript="Kusto: JobErrors"),
    "JobHistory":      R(Text("JobHistory"), rdescript="Kusto: JobHistory"),
    "JobOperations":      R(Text("JobOperations"), rdescript="Kusto: JobOperations"),
    "JobTraces":      R(Text("JobTraces"), rdescript="Kusto: JobTraces"),
    "StorageOperations":      R(Text("StorageOperations"), rdescript="Kusto: StorageOperations"),
    "WorkflowActions":      R(Text("WorkflowActionsAll"), rdescript="Kusto: WorkflowActions"),
    "WorkflowRuns":      R(Text("WorkflowRunsAll"), rdescript="Kusto: WorkflowRuns"),
    "WorkflowDefinitions":      R(Text("WorkflowDefinitionsAll"), rdescript="Kusto: WorkflowDefinitions"),
    "WorkflowTriggers":      R(Text("WorkflowTriggersAll"), rdescript="Kusto: WorkflowTriggers"),

    "where":                        R(Key("enter") + Text("| where "), rdescript="Kusto: Where"),
    "summarize":                        R(Key("enter") + Text("| summarize "), rdescript="Kusto: Where"),
    "take":                        R(Key("enter") + Text("| take 10"), rdescript="Kusto: Where"),
    "Render time chart":    					R(Key("enter") + Text("| render timechart"), rdescript="Kusto: Render timechart"),

    "kusto equals":             R(Text(" == \"\"") + Key("left"), rdescript="Kusto: equals"),
    "contains":             R(Text(" contains \"\"") + Key("left"), rdescript="Kusto: contains"),

    #"[is] greater than":                R(Key("rangle"), rdescript="> Comparison"),
    #"[is] less than":                   R(Key("langle"), rdescript="< Comparison"),

	  "ago":    					R(Text(" ago()") + Key("left"), rdescript="Kusto: ago"),
    "count":    					R(Text(" count()"), rdescript="Kusto: count"),
    "dee count":    					R(Text(" dcount()"), rdescript="Kusto: dcount"),
    "bin":    					R(Text(" bin(TIMESTAMP, 1d)"), rdescript="Kusto: bin"),

    "Run":    					R(Key("f5"), rdescript="Kusto: Run"),
  }
  extras = [
    IntegerRefST("n",1, 10),
  ]
  defaults ={"n": 1}

control.nexus().merger.add_global_rule(KustoRule())

""" context = AppContext(executable="kusto")
grammar = Grammar("Kusto", context=context)

if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
    control.nexus().merger.add_global_rule(KustoRule())
else:
    rule = KustoRule(name="kusto")
    gfilter.run_on(rule)
    grammar.add_rule(rule)
    grammar.load()  """
