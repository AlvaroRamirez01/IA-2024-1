%%  eliza(+Stimuli, -Response) is det.
%   @param  Stimuli is a list of atoms (words).
%   @author Richard A. O'Keefe (The Craft of Prolog)

eliza(Stimuli, Response) :-
    template(InternalStimuli, InternalResponse),
    match(InternalStimuli, Stimuli),
    match(InternalResponse, Response),
    !.

template([s([i,am]),s(X)], [s([why,are,you]),s(X),w('?')]).
template([w(i),s(X),w(you)], [s([why,do,you]),s(X),w(me),w('?')]).
template([s([id,like,to,know,about]),s(X)],[s(X),s([is,a,subject,for,another,session])]).
template([s([i,used,to]),s(X)],[s([did,you,really,enjoy]),s(X),w('?')]).
template([s([i,like]),s(X)],[s([why,do,you,like]),s(X),w('?')]).
template([s([friends,are,so]),s(X)],[s([why,do,you,think,your,friends,are]),s(X),w('?')]).
template([s([id,like,to,have]),s(X)],[s([why,do,you,want,to,have]),s(X),w('?')]).


match([],[]).
match([Item|Items],[Word|Words]) :-
    match(Item, Items, Word, Words).

match(w(Word), Items, Word, Words) :-
    match(Items, Words).
match(s([Word|Seg]), Items, Word, Words0) :-
    append(Seg, Words1, Words0),
    match(Items, Words1).


/** <examples>

?- eliza([i, am, very, hungry], Response).
?- eliza([i, love, you], Response).

*/
