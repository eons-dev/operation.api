import logging
import apie

class operation(apie.Endpoint):
    def __init__(this, name="API Endpoint for any Operation"):
        super().__init__(name)

        this.requiredMethods.append(f"{this.name}_implementation")

        # Everything that can change an operation should be specified in the request...
        this.fetchFrom = [
            'this',
            'args',
			'precursor', # ...but just in case...
            'request_args',
            'request_form',
            'request_json',
            'request_files',
        ]

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return f'''\
------------------------------------
Implemented by {this.precursor.name};
(reminder: you cannot change any variables referenced beyond this point)

{this.precursor.GetHelpText()}
'''

    # Anything you'd like to do before the operation
    def PreOperation(this):
        pass

    # Anything you'd like to do after the operation
    def PostOperation(this):
        pass

    def Call(this):
        this.PreOperation()
        if (this.precursor and hasattr(this.precursor, 'implemented')):
            this.precursor.implemented = this
        eval(f"this.{this.name}_implementation()")
        this.PostOperation()
