from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class NlmQuestions:
    class Meta:
        name = "NLM-QUESTIONS"

    nlm_question: List["NlmQuestions.NlmQuestion"] = field(
        default_factory=list,
        metadata={
            "name": "NLM-QUESTION",
            "type": "Element",
        },
    )

    @dataclass
    class NlmQuestion:
        subject: Optional[str] = field(
            default=None,
            metadata={
                "name": "SUBJECT",
                "type": "Element",
                "required": True,
            },
        )
        message: Optional[str] = field(
            default=None,
            metadata={
                "name": "MESSAGE",
                "type": "Element",
                "required": True,
            },
        )
        sub_questions: Optional["NlmQuestions.NlmQuestion.SubQuestions"] = (
            field(
                default=None,
                metadata={
                    "name": "SUB-QUESTIONS",
                    "type": "Element",
                    "required": True,
                },
            )
        )
        qid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        f_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "fRef",
                "type": "Attribute",
            },
        )

        @dataclass
        class SubQuestions:
            sub_question: List[
                "NlmQuestions.NlmQuestion.SubQuestions.SubQuestion"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "SUB-QUESTION",
                    "type": "Element",
                },
            )

            @dataclass
            class SubQuestion:
                annotations: Optional[
                    "NlmQuestions.NlmQuestion.SubQuestions.SubQuestion.Annotations"
                ] = field(
                    default=None,
                    metadata={
                        "name": "ANNOTATIONS",
                        "type": "Element",
                        "required": True,
                    },
                )
                answers: Optional[
                    "NlmQuestions.NlmQuestion.SubQuestions.SubQuestion.Answers"
                ] = field(
                    default=None,
                    metadata={
                        "name": "ANSWERS",
                        "type": "Element",
                        "required": True,
                    },
                )
                subqid: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass
                class Annotations:
                    focus: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "FOCUS",
                            "type": "Element",
                        },
                    )
                    type_value: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "TYPE",
                            "type": "Element",
                            "required": True,
                        },
                    )

                @dataclass
                class Answers:
                    answer: List[
                        "NlmQuestions.NlmQuestion.SubQuestions.SubQuestion.Answers.Answer"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "ANSWER",
                            "type": "Element",
                        },
                    )

                    @dataclass
                    class Answer:
                        value: str = field(
                            default="",
                            metadata={
                                "required": True,
                            },
                        )
                        answerid: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        pairid: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
